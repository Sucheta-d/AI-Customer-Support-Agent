function LogsTable({ logs }) {
  return (
    <table className="logs-table">
      <thead>
        <tr>
          <th>Refund ID</th>
          <th>Customer</th>
          <th>Order</th>
          <th>Decision</th>
          <th>Reason</th>
          <th>Timestamp</th>
        </tr>
      </thead>

      <tbody>
        {logs.map((log) => (
          <tr key={log.refund_id}>
            <td>{log.refund_id}</td>
            <td>{log.customer_id}</td>
            <td>{log.order_id}</td>

            <td>
              <span
                style={{
                  color:
                    log.decision === "APPROVED"
                      ? "green"
                      : "red",
                  fontWeight: "bold",
                }}
              >
                {log.decision}
              </span>
            </td>

            <td>{log.reason}</td>

            <td>{log.timestamp}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default LogsTable;