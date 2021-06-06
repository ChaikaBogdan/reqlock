import React from "react";
import { BACKEND_URL } from "../constants.js";

const Home = () => {
  const apiUrl = `${BACKEND_URL}/api`;
  const adminUrl = `${BACKEND_URL}`;
  return (
    <nav>
      <ul>
        <li>
          <a href={adminUrl}>Admin</a>
        </li>
        <li>
          <a href={apiUrl}>API</a>
        </li>
      </ul>
    </nav>
  );
};

export default Home;
