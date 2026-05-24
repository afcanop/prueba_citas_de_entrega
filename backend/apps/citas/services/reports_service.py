from django.db.models import Avg, Count, F, ExpressionWrapper
from django.db.models import DurationField

from appointments.models import Appointment


def get_delivery_time_report(date_from, date_to):
    duration_expression = ExpressionWrapper(
        F("delivered_at") - F("scheduled_at"),
        output_field=DurationField(),
    )

    queryset = (
        Appointment.objects.filter(
            status="DELIVERED",
            scheduled_at__date__gte=date_from,
            scheduled_at__date__lte=date_to,
        )
        .annotate(delivery_duration=duration_expression)
        .values("product_line")
        .annotate(
            total_deliveries=Count("id"),
            avg_delivery_time=Avg("delivery_duration"),
        )
        .order_by("product_line")
    )

    return queryset