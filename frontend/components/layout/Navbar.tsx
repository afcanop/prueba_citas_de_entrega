"use client";

import { useState } from "react";
import Sidebar from "./Sidebar";

export default function Navbar() {
  const [open, setOpen] = useState(false);

  const handleLogout = () => {
    document.cookie =
      "access=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

    window.location.href = "/login";
  };

  return (
    <>
      <header className="border-b bg-white px-4 md:px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <button
            className="md:hidden text-2xl"
            onClick={() => setOpen(true)}
          >
            ☰
          </button>

          <h1 className="text-xl font-semibold">
            Sistema de Citas
          </h1>
        </div>

        <button
          onClick={handleLogout}
          className="bg-black text-white px-4 py-2 rounded-lg"
        >
          Salir
        </button>
      </header>

      {open && (
        <div className="fixed inset-0 z-50 bg-black/50 md:hidden">
          <div className="w-64 bg-white h-full">
            <div className="p-4 flex justify-end">
              <button
                onClick={() => setOpen(false)}
                className="text-2xl"
              >
                ×
              </button>
            </div>

            <Sidebar mobile />
          </div>
        </div>
      )}
    </>
  );
}