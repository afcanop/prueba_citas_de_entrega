export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white rounded-xl p-6 border">
          <p className="text-gray-500">
            Programadas
          </p>

          <h2 className="text-3xl font-bold">
            0
          </h2>
        </div>

        <div className="bg-white rounded-xl p-6 border">
          <p className="text-gray-500">
            En proceso
          </p>

          <h2 className="text-3xl font-bold">
            0
          </h2>
        </div>

        <div className="bg-white rounded-xl p-6 border">
          <p className="text-gray-500">
            Entregadas
          </p>

          <h2 className="text-3xl font-bold">
            0
          </h2>
        </div>

        <div className="bg-white rounded-xl p-6 border">
          <p className="text-gray-500">
            Canceladas
          </p>

          <h2 className="text-3xl font-bold">
            0
          </h2>
        </div>
      </div>
    </div>
  );
}