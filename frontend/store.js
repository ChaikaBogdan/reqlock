import { configureStore } from "@reduxjs/toolkit"
import authReducer from "./auth"
import modalReducer from "./modal"
import thunk from "redux-thunk"

export default configureStore({
  reducer: { auth: authReducer, modal: modalReducer },
  middleware: [thunk],
})
