import axios from "axios";
import { useState } from "react";
function isNumeric(val) {
  return /^-?\d+$/.test(val);
}

export default function LinkDevicePage() {
  const [digit, setDigit] = useState("");
  //just check if it is a 4 digit code
  function updateDigit(e) {
    if (e.target.value === "") {
      setDigit(e.target.value);
    }
    if (e.target.value.length <= 4 && isNumeric(e.target.value)) {
      setDigit(e.target.value);
    }
  }
  function submitCode(e) {
    e.preventDefault();
    if (digit.length === 4) {
    }
  }
  return (
    <div className="container text-center">
      <h1>Link Device</h1>
      <form onSubmit={(e) => submitCode(e)}>
        <input
          value={digit}
          onChange={(e) => updateDigit(e)}
          style={{ width: "200px", fontSize: "70px", textAlign: "center" }}
        ></input>
      </form>
    </div>
  );
}
