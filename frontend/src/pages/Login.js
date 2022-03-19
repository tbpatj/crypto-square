import { useState } from "react";
import { Link } from "react-router-dom";
import useRegister from "../hooks/RegisterHook";

export default function Login() {
  const { email, password, updateInput, submit } = useRegister();
  return (
    <div>
      <Link to="/">
        <p>back</p>
      </Link>
      <div className="center-column">
        <h1 className="">Login</h1>
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
                type="password"
                value={password}
                onChange={(e) => updateInput(e, "password")}
              ></input>
            </label>
            {/* submit button */}
            <button onClick={(e) => submit(e, "login")}>submit</button>
          </div>
        </div>
      </form>
    </div>
  );
}
