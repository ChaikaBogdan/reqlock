import React from "react";
import ReactDOM from "react-dom";
import { useFormik } from "formik";
import * as yup from "yup";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
// import Button from "react-bootstrap";
// import TextField from "react-bootstrap";
import { BACKEND_URL } from "../constants.js";
import axios from "axios";

const signInURL = `${BACKEND_URL}/dj-rest-auth/login/`;

const validationSchema = yup.object({
  email: yup
    .string("Enter your email")
    .email("Enter a valid email")
    .required("Email is required"),
  password: yup
    .string("Enter your password")
    .min(4, "Password should be of minimum 8 characters length")
    .required("Password is required"),
});

export const SignIn = () => {
  const formik = useFormik({
    initialValues: {
      email: "user@reqlock.com",
      password: "user123",
    },
    validationSchema: validationSchema,
    onSubmit: (values) => {
      console.log(values);
      axios
        .post(`${signInURL}`, values)
        .then((res) => {
          alert(JSON.stringify(res, null, 2));
        })
        .catch((error) => {
          alert(JSON.stringify(error.response.data, null, 2));
        });
    },
  });

  return (
    <div>
      <form onSubmit={formik.handleSubmit}>
        <TextField
          id="email"
          name="email"
          label="Email"
          value={formik.values.email}
          onChange={formik.handleChange}
          error={formik.touched.email && Boolean(formik.errors.email)}
          helperText={formik.touched.email && formik.errors.email}
        />
        <TextField
          id="password"
          name="password"
          label="Password"
          type="password"
          value={formik.values.password}
          onChange={formik.handleChange}
          error={formik.touched.password && Boolean(formik.errors.password)}
          helperText={formik.touched.password && formik.errors.password}
        />
        <Button color="primary" variant="contained" type="submit">
          Submit
        </Button>
      </form>
    </div>
  );
};
