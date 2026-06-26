function TracePanel({ trace }) {
  if (!trace || trace.length === 0) return null;

  return (
    <div className="card">
      <h2>🤖 Agent Reasoning</h2>

      <div className="trace-container">
        {trace.map((step, index) => (
          <div key={index} className="trace-step">
            <span className="trace-icon">✔</span>
            <span>{step}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default TracePanel;