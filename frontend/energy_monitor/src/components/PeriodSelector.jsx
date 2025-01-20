import { useState } from "react";

const PeriodSelector = ({ onPeriodChange }) => {
  const [selectedPeriod, setSelectedPeriod] = useState("today");

  const handlePeriodClick = (period) => {
    setSelectedPeriod(period); // Update the selected period locally
    onPeriodChange(period); // Notify the parent
  };

  return (
    <div className="period-selector">
      {["today", "month", "year"].map((period) => (
        <button
          key={period}
          className={`period-btn ${selectedPeriod === period ? "active" : ""}`}
          onClick={() => handlePeriodClick(period)}
        >
          {period.charAt(0).toUpperCase() + period.slice(1)}
        </button>
      ))}
    </div>
  );
};

export default PeriodSelector;
