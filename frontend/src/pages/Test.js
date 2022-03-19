import axios from "axios";

export default function Test() {
  function hitServer() {
    console.log("sending to server a get request on /test/");
    axios
      .get("http://localhost:8000/test/")
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  }

  return (
    <div>
      <h1>YEah</h1>
      <button onClick={(e) => hitServer()}></button>
    </div>
  );
}
