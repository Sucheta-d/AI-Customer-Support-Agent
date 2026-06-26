import { useState } from "react";

function RefundForm({ onSubmit, loading }) {
  const [customerId, setCustomerId] = useState("");
  const [orderId, setOrderId] = useState("");
  const [reason, setReason] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit({
      customer_id: Number(customerId),
      order_id: Number(orderId),
      reason: reason,
    });
  };

  return (
    <div className="card">
      <h2>Request Refund</h2>

      <form onSubmit={handleSubmit}>

        <label>Customer ID</label>
        <input
          type="number"
          value={customerId}
          onChange={(e) => setCustomerId(e.target.value)}
          required
        />

        <label>Order ID</label>
        <input
          type="number"
          value={orderId}
          onChange={(e) => setOrderId(e.target.value)}
          required
        />

        <label>Reason</label>
        <textarea
          rows="4"
          value={reason}
          onChange={(e) => setReason(e.target.value)}
          required
        />

        <button
          type="submit"
          disabled={loading}
        >
          {loading ? "Processing..." : "Submit Refund"}
        </button>

      </form>
    </div>
  );
}

export default RefundForm;