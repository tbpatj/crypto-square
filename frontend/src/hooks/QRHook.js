import axios from "axios";
import { useEffect, useState } from "react";

export default function useQR() {
  const [loggedIn, setLoggedIn] = useState(true);
  const [intervalTimer, setIntervalTimer] = useState(-1);
  const [QRByte, setQRByte] = useState(null);
  const [status, setStatus] = useState(0);

  function checkForQR() {
    console.log("checking server");
    axios
      .get(
        `http://192.168.1.18:8000/api/qr?merchant_id=${localStorage.getItem(
          "merchant_id"
        )}&qr_recieved=${localStorage.getItem("qr_recieved")}`
      )
      .then((res) => {
        console.log(res.data);
        if (!res.data.message && !res.data.state) {
          //get that QR code
          console.log(res.data[0]);
          setQRByte(res.data[0].image);
          setStatus(1);
          localStorage.setItem("qr_recieved", true);
          console.log("clearing interval timer", intervalTimer);
          clearInterval(intervalTimer);
        } else if (res.data.state) {
          setStatus(2);
          if (res.data.state === "Transaction complete") {
            setStatus(3);
          }
        } else {
          console.log("not yet");
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }
  //when the component mounts set up an interval timer for checking the backend for new QR codes
  useEffect(() => {
    localStorage.setItem("qr_recieved", false);
    let intervalID = setInterval(() => {
      if (status === 0) {
        checkForQR();
      } else if (status === 1) {
      }
      //hit the django server to see if we got a code or any update
    }, 5000);
    if (status === 0) {
      checkForQR();
    } else if (status === 1) {
    }
    console.log("interval timer ID " + intervalID);
    setIntervalTimer(intervalID);
    //clear the interval timer when the component unmounts
    return () => clearInterval(intervalID);
  }, []);

  return { loggedIn, QRByte, status };
}
