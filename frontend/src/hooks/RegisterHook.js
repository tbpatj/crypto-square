import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export default function useRegister() {
  let navigate = useNavigate();
  //this react hook will store all of our states
  const [email, setEmail] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [stripe, setStripe] = useState("");
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
      case "stripe":
        setStripe(e.target.value);
        return true;
      default:
        return false;
    }
  }

  function submit(e, subject) {
    e.preventDefault();

    if (subject === "register") {
      //submit axios calls
      let body = {
        username: email,
        email: email,
        password: password,
        first_name: firstname,
        last_name: lastname,
        stripe_id: stripe,
      };
      console.log("Registering user");
      axios.post("http://127.0.0.1:8000/register/", body).then((res) => {
        if (res.data.status === "success") {
          console.log("setting user ID " + res.data.user_id);
          localStorage.setItem("user_id", res.data.user_id);
          console.log("setting merchant ID " + res.data.merchant_id);
          localStorage.setItem("merchant_id", res.data.merchant_id);
          navigate("../", { replace: true });
        } else {
          console.log("no success message recieved");
        }
      });
    } else if (subject === "login") {
      let body = {
        email: email,
        password: password,
      };
      console.log("Logging in User");
      axios.post("http://127.0.0.1:8000/login/", body).then((res) => {
        console.log(res);
        if (res.data.status === "success") {
          console.log("user_id stored");
          navigate("/", { replace: true });
          localStorage.setItem("user_id", res.data.user_id);
        } else {
          console.log("no message of success returned");
        }
      });
    }
  }

  //export the states and functions so we only get what we need in the Register component. makes it clean 👌
  return { email, firstname, lastname, stripe, password, updateInput, submit };
}
