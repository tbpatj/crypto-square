import { useState } from "react";
import useRegister from "../hooks/RegisterHook";

export default function Login() {
  const { email, password, updateInput, submit } = useRegister();
  return (
    <div>
      <h1>Register</h1>
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
