import { createSlice } from "@reduxjs/toolkit"

export const authSlice = createSlice({
  name: "auth",
  initialState: {
    auth: {},
    message: {},
    isLoaded: false,
  },
  reducers: {
    SET_AUTH: (state, action) => {
      state.auth = action.payload
    },
    SET_MESSAGE: (state, action) => {
      state.message = action.payload
    },
    SET_LOADED: (state) => {
      state.isLoaded = true
    },
  },
})

export const { SET_AUTH, SET_MESSAGE, SET_LOADED } = authSlice.actions

export default authSlice.reducer
