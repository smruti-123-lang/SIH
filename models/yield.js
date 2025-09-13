"use client";
import { useState } from "react";

export default function YieldForm() {
  const [form, setForm] = useState({
    State: "",
    Crop: "",
    Season: "",
    Area: "",
    Crop_Year: "",
    Production: "",
    Annual_Rainfall: "",
    Fertilizer: "",
    Pesticide: "",
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("/api/yieldRoute", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="p-6 max-w-lg mx-auto bg-white shadow rounded">
      <h2 className="text-xl font-bold mb-4">Crop Yield Prediction</h2>
      <form onSubmit={handleSubmit} className="space-y-3">
        {Object.keys(form).map((key) => (
          <div key={key}>
            <label className="block font-medium">{key}</label>
            <input
              type="text"
              name={key}
              value={form[key]}
              onChange={handleChange}
              className="w-full border rounded px-2 py-1"
              required
            />
          </div>
        ))}
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          Predict
        </button>
      </form>

      {result && (
        <div className="mt-4 p-3 bg-gray-100 rounded">
          {result.predicted_yield ? (
            <p>
              ✅ Predicted Yield:{" "}
              <b>{result.predicted_yield.toFixed(2)}</b>
            </p>
          ) : (
            <p className="text-red-600">❌ Error: {result.error}</p>
          )}
        </div>
      )}
    </div>
  );
}
