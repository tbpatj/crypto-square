import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function Homepage() {
  const [userID, setUserID] = useState(null);
  useEffect(() => {
    let user_id = localStorage.getItem("user_id");
    if (user_id === null) {
      setUserID(user_id);
    }
  });
  return (
    <div>
      <div className="jumbotron text-center">
        <h1>Welcome to Crypto Square</h1>

        {userID !== null ? (
          <div>
            <p>Click to join now</p>
            <Link to={"/register"}>
              <button className="btn btn-primary">Sign Up</button>
            </Link>
          </div>
        ) : (
          <div>
            <br></br>
            <p>logged in</p>
          </div>
        )}
      </div>
      <div className="container">
        <h1>Homepage</h1>
        <p>welcome to our homepage</p>
      </div>
    </div>
  );
}
