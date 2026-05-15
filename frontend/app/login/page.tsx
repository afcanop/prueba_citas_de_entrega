"use client";

import { useState } from "react";
import { api } from "@/services/api";
import { setItemLocalStorage  } from "@/services/localStorage.service";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      const response = await api.post("/token/", {
        username,
        password,
      });

      document.cookie = `access=${response.data.access}; path=/`;

      window.location.href = "/dashboard";
    } catch (error) {
      console.error(error);
      alert("Credenciales inválidas");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-sm space-y-4 border rounded-xl p-6">
        <h1 className="text-2xl font-bold">Login</h1>

        <input
          className="w-full border p-2 rounded"
          placeholder="Usuario"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          className="w-full border p-2 rounded"
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={handleLogin}
          className="w-full bg-black text-white p-2 rounded"
        >
          Ingresar
        </button>
      </div>
    </div>
  );
}