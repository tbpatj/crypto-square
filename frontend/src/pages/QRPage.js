import { useState } from "react";
import useQR from "../hooks/QRHook";

export default function QRPage() {
  const { loggedIn, QRByte, status } = useQR();
  //if the user has logged in with a code
  console.log(loggedIn);
  if (loggedIn) {
    return (
      <div className="text-center">
        <h1>QR Generator</h1>
        {status === 0 && (
          <div>
            <h1>Waiting for Transaction</h1>
          </div>
        )}
        {status === 1 && (
          <img src={`data:image/png;base64,${QRByte}`} alt="none"></img>
        )}
        {/* QR will go down here */}
        {status === 2 && (
          <div className="container my-relative">
            <div className="spin"></div>
            <h4>Processing</h4>
          </div>
        )}
        {status === 3 && (
          <div>
            <img
              src="https://im2.ezgif.com/tmp/ezgif-2-f34f47400e.gif"
              alt="none"
            ></img>
            <div className="text-center">
              <h2>Vendor Payed</h2>
            </div>
          </div>
        )}
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
