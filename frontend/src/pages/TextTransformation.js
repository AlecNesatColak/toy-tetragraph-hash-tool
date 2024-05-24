import React, { useState } from "react";
import axios from "axios";

function TextTransformation() {
  const [inputText, setInputText] = useState("");
  const [steps, setSteps] = useState([]);
  const [finalResult, setFinalResult] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/transform/", {
        text: inputText,
      });
      const { steps, final_running_total } = response.data;
      setSteps(steps);
      setFinalResult(final_running_total);
      setError("");
    } catch (error) {
      console.error("Error fetching data: ", error);
      setError("Failed to fetch results. Please try again.");
      setSteps([]);
      setFinalResult("");
    }
  };

  const renderMatrix = (matrix) => (
    <table className="matrix-table">
      <tbody>
        {matrix.map((row, rowIndex) => (
          <tr key={rowIndex}>
            {row.map((item, colIndex) => (
              <td key={colIndex}>{item}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );

  return (
    <div className="container">
      <h1>Text Transformation Tool</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="inputText">Enter Text:</label>
          <textarea
            className="form-control"
            id="inputText"
            value={inputText}
            onChange={handleChange}
            rows="3"
          ></textarea>
        </div>
        <button type="submit" className="btn btn-primary">
          Transform
        </button>
      </form>
      {error && (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      )}
      {steps.length > 0 && (
        <div className="results">
          <h2>Transformation Steps:</h2>
          {steps.map((step, index) => (
            <div key={index} className="step">
              <h3>Step {index + 1}</h3>
              <div className="matrix-wrapper">
                <p>Original Alpha Matrix:</p>
                {renderMatrix(step.original_alpha_matrix)}
              </div>
              <div className="matrix-wrapper">
                <p>Original Numeric Matrix:</p>
                {renderMatrix(step.original_numeric_matrix)}
              </div>
              <p>
                Running Total After Initial Matrix:{" "}
                {JSON.stringify(step.running_total_after_initial)}
              </p>
              <div className="matrix-wrapper">
                <p>Transformed Alpha Matrix:</p>
                {renderMatrix(step.transformed_alpha_matrix)}
              </div>
              <div className="matrix-wrapper">
                <p>Transformed Numeric Matrix:</p>
                {renderMatrix(step.transformed_numeric_matrix)}
              </div>
              <p>
                Running Total After Transformation:{" "}
                {JSON.stringify(step.running_total_after_transformation)}
              </p>
            </div>
          ))}
          <h2>Final Running Total (Alphabetic): {finalResult}</h2>
        </div>
      )}
    </div>
  );
}

export default TextTransformation;
