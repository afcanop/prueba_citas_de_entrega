"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  {
    label: "Dashboard",
    href: "/dashboard",
  },
  {
    label: "Citas",
    href: "/citas",
  },
  {
    label: "Reportes",
    href: "/reportes",
  },
];

interface Props {
  mobile?: boolean;
}

export default function Sidebar({
  mobile = false,
}: Props) {
  const pathname = usePathname();

  return (
    <aside
      className={`
        bg-white border-r
        ${mobile ? "w-full" : "hidden md:block w-64"}
      `}
    >
      <div className="p-6">
        <h2 className="text-2xl font-bold mb-8">
          Gestión Citas
        </h2>

        <nav className="space-y-2">
          {links.map((link) => {
            const isActive =
              pathname === link.href;

            return (
              <Link
                key={link.href}
                href={link.href}
                className={`
                  block rounded-lg px-4 py-3 transition
                  ${
                    isActive
                      ? "bg-black text-white"
                      : "hover:bg-gray-100"
                  }
                `}
              >
                {link.label}
              </Link>
            );
          })}
        </nav>
      </div>
    </aside>
  );
}