import { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Homepage from "../pages/Homepage";
import LinkDevicePage from "../pages/LinkDevice";
import Login from "../pages/Login";
import QRPage from "../pages/QRPage";
import Register from "../pages/Register";
import Test from "../pages/Test";
function NavBar() {
  const [userID, setUserID] = useState(null);
  useEffect(() => {
    let user_id = localStorage.getItem("user_id");
    if (user_id === null) {
      console.log("set user ID" + user_id);
      setUserID(user_id);
    }
    setUserID(user_id);
    console.log(user_id);
  }, []);

  return (
    <nav className="float-right">
      {(window.location.pathname !== "/login" ||
        window.location.pathname !== "/QR") &&
        userID === null && (
          <Link to="/login">
            <button className="btn btn-secondary">Log In</button>
          </Link>
        )}
      {userID !== null && window.location.pathname !== "/QR" && (
        <nav className="float-right">
          <Link to="/deviceconf">
            <button className="btn btn-secondary">Link Device</button>
          </Link>
        </nav>
      )}
    </nav>
  );
}

export default function MainAppComponent() {
  //add in the router and other main configures
  return (
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" exact element={<Homepage />}></Route>
        <Route path="/register" element={<Register />}></Route>
        <Route path="/login" element={<Login />}></Route>
        <Route path="/test" element={<Test />}></Route>
        <Route path="/QR" element={<QRPage />}></Route>
        <Route path="/deviceconf" element={<LinkDevicePage />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
