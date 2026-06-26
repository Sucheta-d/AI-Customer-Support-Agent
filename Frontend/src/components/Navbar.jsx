import { Link, useLocation } from "react-router-dom";

function Navbar() {
  const location = useLocation();

  return (
    <nav className="navbar">
      <h2>🤖 AI Customer Support Agent</h2>

      <div>
        <Link
          className={
            location.pathname === "/"
              ? "active-link"
              : ""
          }
          to="/"
        >
          Customer
        </Link>

        <Link
          className={
            location.pathname === "/dashboard"
              ? "active-link"
              : ""
          }
          to="/dashboard"
        >
          Dashboard
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;