function DashboardStats({ logs }) {
  const approved = logs.filter(
    (log) => log.decision === "APPROVED"
  ).length;

  const denied = logs.filter(
    (log) => log.decision === "DENIED"
  ).length;

  return (
    <div className="stats">
      <div className="stat-card">
        <h3>Total Refunds</h3>
        <h1>{logs.length}</h1>
      </div>

      <div className="stat-card">
        <h3>Approved</h3>
        <h1>{approved}</h1>
      </div>

      <div className="stat-card">
        <h3>Denied</h3>
        <h1>{denied}</h1>
      </div>
    </div>
  );
}

export default DashboardStats;