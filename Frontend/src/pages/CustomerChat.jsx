import RefundForm from "../components/RefundForm";
import DecisionCard from "../components/DecisionCard";
import TracePanel from "../components/TracePanel";

import useRefund from "../hooks/useRefund";

function CustomerChat() {

  const {
    loading,
    result,
    error,
    submitRefund,
  } = useRefund();

  return (
    <div className="container">

      <h1>AI Customer Support Agent</h1>

      <RefundForm
        onSubmit={submitRefund}
        loading={loading}
      />

      {error && (
        <p style={{ color: "red" }}>
          {error}
        </p>
      )}

      <DecisionCard result={result} />

      <TracePanel trace={result?.trace} />

    </div>
  );
}

export default CustomerChat;