import { useState } from "react";
import useQR from "../hooks/QRHook";

export default function QRPage() {
  const { loggedIn, QRByte } = useQR();
  //if the user has logged in with a code
  console.log(loggedIn);
  if (loggedIn) {
    return (
      <div className="text-center">
        <h1>QR Generator</h1>
        <img src={`data:image/png;base64,${QRByte}`} alt="none"></img>
        {/* QR will go down here */}
      </div>
    );
  }
  //if the user hasn't set up the POS system here is where they would enter the code
  return (
    <div>
      <input type="number" placeholder="Enter Code"></input>
    </div>
  );
}
