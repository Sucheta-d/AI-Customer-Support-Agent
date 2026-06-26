
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import CustomerChat from "./pages/CustomerChat";
import AdminDashboard from "./dashboard/AdminDashboard";
import Navbar from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>

      <nav
        style={{
          padding: "20px",
          background: "#2563eb",
        }}
      >
        <Link
          to="/"
          style={{
            color: "white",
            marginRight: "20px",
            textDecoration: "none",
          }}
        >
          Customer Chat
        </Link>

        <Link
          to="/dashboard"
          style={{
            color: "white",
            textDecoration: "none",
          }}
        >
          Admin Dashboard
        </Link>
      </nav>

      <Routes>
        <Route path="/" element={<CustomerChat />} />
        <Route
          path="/dashboard"
          element={<AdminDashboard />}
        />
      </Routes>

    </BrowserRouter>
  );
}

export default App;