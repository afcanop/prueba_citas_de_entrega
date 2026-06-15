"use client";

import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Container,
  Box,
  Grid,
  Card,
  CardContent,
} from "@mui/material";
import Link from "next/link";

export default function LandingPage() {
  return (
    <Box sx={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}>
      <AppBar position="static" elevation={0}>
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1, fontWeight: 700 }}>
            Sistema de Citas
          </Typography>
          <Button color="inherit" component={Link} href="/login">
            Iniciar Sesión
          </Button>
        </Toolbar>
      </AppBar>

      <Box
        sx={{
          bgcolor: "primary.main",
          color: "white",
          py: { xs: 8, md: 12 },
          textAlign: "center",
        }}
      >
        <Container maxWidth="md">
          <Typography variant="h3" sx={{ fontWeight: 700 }} gutterBottom>
            Gestión de Citas de Entrega
          </Typography>
          <Typography variant="h6" sx={{ mb: 4, opacity: 0.9 }}>
            Administra, programa y da seguimiento a tus citas de entrega de
            forma sencilla y eficiente.
          </Typography>
          <Button
            variant="contained"
            color="secondary"
            size="large"
            component={Link}
            href="/login"
          >
            Comenzar
          </Button>
        </Container>
      </Box>

      <Container maxWidth="lg" sx={{ py: 8 }}>
        <Typography variant="h4" sx={{ fontWeight: 600, textAlign: "center" }} gutterBottom>
          ¿Qué ofrecemos?
        </Typography>
        <Grid container spacing={4} sx={{ mt: 2 }}>
          {[
            {
              title: "Programación",
              desc: "Agenda citas de entrega de manera rápida y organizada.",
            },
            {
              title: "Seguimiento",
              desc: "Da seguimiento en tiempo real al estado de cada cita.",
            },
            {
              title: "Reportes",
              desc: "Genera reportes detallados sobre las entregas realizadas.",
            },
          ].map((item) => (
            <Grid size={{ xs: 12, md: 4 }} key={item.title}>
              <Card elevation={2}>
                <CardContent sx={{ p: 4, textAlign: "center" }}>
                  <Typography variant="h5" sx={{ fontWeight: 600 }} gutterBottom>
                    {item.title}
                  </Typography>
                  <Typography color="text.secondary">{item.desc}</Typography>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Container>

      <Box
        component="footer"
        sx={{ bgcolor: "grey.900", color: "white", py: 3, mt: "auto" }}
      >
        <Container maxWidth="lg">
          <Typography variant="body2" sx={{ textAlign: "center" }}>
            &copy; {new Date().getFullYear()} Sistema de Citas. Todos los
            derechos reservados.
          </Typography>
        </Container>
      </Box>
    </Box>
  );
}
