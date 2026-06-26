function DecisionCard({ result }) {
  if (!result) return null;

  const approved = result.decision === "APPROVED";

  return (
    <div className="card">

      <h2>AI Decision</h2>

      <div
        style={{
          padding: "15px",
          borderRadius: "10px",
          background: approved ? "#dcfce7" : "#fee2e2",
          color: approved ? "#166534" : "#991b1b",
          fontWeight: "bold",
          fontSize: "22px",
          textAlign: "center"
        }}
      >
        {approved ? "✅ APPROVED" : "❌ DENIED"}
      </div>

      <h3 style={{ marginTop: "20px" }}>
        Explanation
      </h3>

      <p>{result.reason}</p>

    </div>
  );
}

export default DecisionCard;