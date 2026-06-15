"use client";

import { useState } from "react";
import {
  Container,
  Box,
  Typography,
  TextField,
  Button,
  Paper,
} from "@mui/material";
import { api } from "@/services/api";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      // const response = await api.post("/token/", {
      //   username,
      //   password,
      // });

      document.cookie = `access=123; path=/`;

      window.location.href = "/dashboard";
    } catch (error) {
      console.error(error);
      alert("Credenciales inválidas");
    }
  };

  return (
    <Container maxWidth="xs" sx={{ minHeight: "100vh", display: "flex", alignItems: "center" }}>
      <Paper elevation={3} sx={{ p: 4, width: "100%" }}>
        <Typography variant="h5" sx={{ fontWeight: 700, textAlign: "center" }} gutterBottom>
          Iniciar Sesión
        </Typography>

        <Box component="form" sx={{ mt: 2, display: "flex", flexDirection: "column", gap: 2 }}>
          <TextField
            label="Usuario"
            variant="outlined"
            fullWidth
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextField
            label="Contraseña"
            type="password"
            variant="outlined"
            fullWidth
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button variant="contained" size="large" fullWidth onClick={handleLogin}>
            Ingresar
          </Button>
        </Box>
      </Paper>
    </Container>
  );
}
