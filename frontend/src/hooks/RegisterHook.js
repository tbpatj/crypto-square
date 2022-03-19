import { useState } from "react";

export default function useRegister() {
  //this react hook will store all of our states
  const [email, setEmail] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [plaid, setPlaid] = useState("");
  const [password, setPassword] = useState("");

  //function that we pass out of our hook to make input fields a little cleaner in react
  function updateInput(e, name) {
    switch (name) {
      case "email":
        console.log("email");
        setEmail(e.target.value);
        return true;
      case "password":
        setPassword(e.target.value);
        return true;
      case "firstname":
        setFirstname(e.target.value);
        return true;
      case "lastname":
        setLastname(e.target.value);
        return true;
      case "plaid":
        setPlaid(e.target.value);
        return true;
      default:
        return false;
    }
  }

  function submit() {
    //submit axios calls
  }

  //export the states and functions so we only get what we need in the Register component. makes it clean 👌
  return { email, firstname, lastname, plaid, password, updateInput, submit };
}
