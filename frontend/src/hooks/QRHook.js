import axios from "axios";
import { useEffect, useState } from "react";

export default function useQR() {
  const [loggedIn, setLoggedIn] = useState(true);
  const [QRByte, setQRByte] = useState(null);
  const [status, setStatus] = useState(-1);
  //when the component mounts set up an interval timer for checking the backend for new QR codes
  useEffect(() => {
    axios.get("http://localhost:8000/api/qr").then((res) => {
      console.log(res.data[0]);
      setQRByte(res.data[0].image);
      setStatus(1);
    });
    let intervalID = setInterval(() => {
      //hit the django server to see if we got a code or any update
    }, 5000);

    //clear the interval timer when the component unmounts
    return () => clearInterval(intervalID);
  }, []);

  return { loggedIn, QRByte, status };
}
