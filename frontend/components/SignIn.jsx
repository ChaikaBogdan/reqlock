import React from "react"
import { useFormik } from "formik"
import * as yup from "yup"
import Button from "@material-ui/core/Button"
import TextField from "@material-ui/core/TextField"
import { BACKEND_URL } from "../constants.js"
import { useHistory } from "react-router-dom"
import axios from "axios"

const signInURL = `${BACKEND_URL}/dj-rest-auth/login/`

const validationSchema = yup.object({
  email: yup
    .string("Enter your email")
    .email("Enter a valid email")
    .required("Email is required"),
  password: yup
    .string("Enter your password")
    .min(4, "Password should be of minimum 8 characters length")
    .required("Password is required"),
})

export const SignIn = (props) => {
  const history = useHistory()
  const formik = useFormik({
    initialValues: {
      email: "user@reqlock.com",
      password: "user123",
    },
    validationSchema,
    onSubmit: values => {
      axios
        .post(signInURL, values)
        .then(({data}) => {
          console.info(data)
          const {access_token: token, user} = data
          const {username, email, pk} = user
          const auth = JSON.stringify({token, username, email, pk})
          localStorage.setItem('auth', auth)
          history.push('/');
          console.info('Login');
        })
        .catch(error => {
          console.error(error)
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
  )
}
