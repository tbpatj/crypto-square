import { useState } from "react";
import useRegister from "../hooks/RegisterHook";

export default function Register() {
  const { email, firstname, lastname, plaid, password, updateInput } =
    useRegister();
  return (
    <div>
      <h1>Register</h1>
      <form>
        <div className="center-column">
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
              placeholder="plaid"
              value={plaid}
              onChange={(e) => updateInput(e, "plaid")}
            ></input>
          </label>

          {/* submit button */}
          <button>submit</button>
        </div>
      </form>
    </div>
  );
}
