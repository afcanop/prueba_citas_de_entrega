"use client";

import {
  Typography,
  Grid,
  Card,
  CardContent,
  Box,
} from "@mui/material";
import EventNoteIcon from "@mui/icons-material/EventNote";
import PlayCircleIcon from "@mui/icons-material/PlayCircle";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";

const stats = [
  { label: "Programadas", value: 0, icon: <EventNoteIcon />, color: "#1976d2" },
  { label: "En proceso", value: 0, icon: <PlayCircleIcon />, color: "#f57c00" },
  { label: "Entregadas", value: 0, icon: <CheckCircleIcon />, color: "#388e3c" },
  { label: "Canceladas", value: 0, icon: <CancelIcon />, color: "#d32f2f" },
];

export default function DashboardPage() {
  return (
    <Box>
      <Typography variant="h4" sx={{ fontWeight: 700 }} gutterBottom>
        Dashboard
      </Typography>

      <Grid container spacing={3}>
        {stats.map((stat) => (
          <Grid size={{ xs: 12, sm: 6, md: 3 }} key={stat.label}>
            <Card elevation={2}>
              <CardContent sx={{ display: "flex", alignItems: "center", gap: 2 }}>
                <Box sx={{ color: stat.color, fontSize: 40 }}>
                  {stat.icon}
                </Box>
                <Box>
                  <Typography variant="body2" color="text.secondary">
                    {stat.label}
                  </Typography>
                  <Typography variant="h4" sx={{ fontWeight: 700 }}>
                    {stat.value}
                  </Typography>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}
