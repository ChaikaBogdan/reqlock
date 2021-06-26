import React from "react"
import { useFormik } from "formik"
import * as yup from "yup"
import Button from "@material-ui/core/Button"
import TextField from "@material-ui/core/TextField"
import { BACKEND_URL } from "../constants.js"
import axios from "axios"
import { useHistory } from 'react-router-dom'

const signUpURL = `${BACKEND_URL}/dj-rest-auth/registration/`
const validationSchema = yup.object({
  email: yup
    .string("Enter your email")
    .email("Enter a valid email")
    .required("Email is required"),
  password1: yup
    .string("Enter your password")
    .min(4, "Password should be of minimum 8 characters length")
    .required("Password is required"),
  password2: yup
    .string("Verify your password")
    .min(4, "Password should be of minimum 8 characters length")
    .required("Password is required"),
})

export const SignUp = () => {
  const history = useHistory()
  const formik = useFormik({
    initialValues: {
      email: "user@reqlock.com",
      password1: "user123",
      password2: "user123",
    },
    validationSchema,
    onSubmit: values => {
      axios
        .post(signUpURL, values)
        .then(res => {
          history.push('/signin')
        })
        .catch(error => console.error(error))
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
          id="password1"
          name="password1"
          label="Password"
          type="password"
          value={formik.values.password1}
          onChange={formik.handleChange}
          error={formik.touched.password && Boolean(formik.errors.password)}
          helperText={formik.touched.password && formik.errors.password}
        />
        <TextField
          id="password2"
          name="password2"
          label="Verify"
          type="password"
          value={formik.values.password2}
          onChange={formik.handleChange}
          error={formik.touched.password && Boolean(formik.errors.password)}
          helperText={formik.touched.password && formik.errors.password}
        />
        <Button color="primary" variant="contained" type="submit">
          Submit
        </Button>
      </form>
    </div>
  )
}
