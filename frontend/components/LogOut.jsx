import React, { useState, useEffect } from "react";
import { BACKEND_URL } from "../constants.js";
import axios from "axios";

const logOutURL = `${BACKEND_URL}/dj-rest-auth/logout/`;

export const LogOut = () => {
  useEffect(() => {
    console.log("LOGOUT");
    axios
      .post(`${logOutURL}`)
      .then((res) => {
        alert(JSON.stringify(res, null, 2));
      })
      .catch((error) => {
        alert(JSON.stringify(error.response.data, null, 2));
      });
  }, []);

  return null;
};
