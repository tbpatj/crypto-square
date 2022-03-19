import { useState } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Homepage from "../pages/Homepage";
import Login from "../pages/Login";
import QRPage from "../pages/QRPage";
import Register from "../pages/Register";
import Test from "../pages/Test";
function NavBar() {
  return (
    <nav className="float-right">
      {window.location.pathname !== "/login" && (
        <Link to="/login">
          <button className="btn btn-secondary">Log In</button>
        </Link>
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
      </Routes>
    </BrowserRouter>
  );
}
