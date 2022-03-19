import { useState } from "react";
import { Link } from "react-router-dom";
import useRegister from "../hooks/RegisterHook";

export default function Register() {
  const { email, firstname, lastname, stripe, password, updateInput, submit } =
    useRegister();
  return (
    <div>
      <Link to="/">
        <p>back</p>
      </Link>
      <div className="center-column">
        <h1 className="">Registration</h1>
      </div>
      <form>
        <div className="center-column">
          <div className="left">
            {" "}
            {/* email input field */}
            <label>
              <span>email</span>
              <input
                placeholder="email"
                value={email}
                onChange={(e) => updateInput(e, "email")}
              ></input>
            </label>
            {/* password input field */}
            <label>
              <span>password</span>
              <input
                placeholder="password"
                value={password}
                type="password"
                onChange={(e) => updateInput(e, "password")}
              ></input>
            </label>
            {/* firstname input field */}
            <label>
              <span>firstname</span>
              <input
                placeholder="firstname"
                value={firstname}
                onChange={(e) => updateInput(e, "firstname")}
              ></input>
            </label>
            {/* lastname input field */}
            <label>
              <span>lastname</span>
              <input
                placeholder="lastname"
                value={lastname}
                onChange={(e) => updateInput(e, "lastname")}
              ></input>
            </label>
            {/* plaid input field */}
            <label>
              <span>plaid</span>
              <input
                type="number"
                placeholder="stripe ID"
                value={stripe}
                onChange={(e) => updateInput(e, "stripe")}
              ></input>
            </label>
            {/* submit button */}
            <button onClick={(e) => submit(e, "register")}>submit</button>
          </div>
        </div>
      </form>
    </div>
  );
}
