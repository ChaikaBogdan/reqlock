import { configureStore } from "@reduxjs/toolkit"
import authReducer from "./auth"
import thunk from "redux-thunk"

export default configureStore({
  reducer: { auth: authReducer },
  middleware: [thunk],
})
