"use client";

import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { ReactNode } from "react";

const theme = createTheme({
  cssVariables: true,
  colorSchemes: {
    light: {
      palette: {
        primary: { main: "#6750A4" },
        secondary: { main: "#625B71" },
        background: { default: "#FFFBFE", paper: "#FFFBFE" },
      } as any,
    },
    dark: {
      palette: {
        primary: { main: "#D0BCFF" },
        secondary: { main: "#CCC2DC" },
        background: { default: "#1C1B1F", paper: "#1C1B1F" },
      } as any,
    },
  },
  shape: { borderRadius: 12 },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
  },
});

export default function MuiThemeProvider({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      {children}
    </ThemeProvider>
  );
}
