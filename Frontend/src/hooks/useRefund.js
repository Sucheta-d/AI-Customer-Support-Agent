import { useState } from "react";
import api from "../services/api";

export default function useRefund() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const submitRefund = async (refundData) => {
    setLoading(true);
    setError("");

    try {
      const response = await api.post("/refund", refundData);
      setResult(response.data);
    } catch (err) {
      console.error(err);

      setError(
        err.response?.data?.detail ||
          "Unable to process refund request."
      );
    } finally {
      setLoading(false);
    }
  };

  return {
    loading,
    result,
    error,
    submitRefund,
  };
}