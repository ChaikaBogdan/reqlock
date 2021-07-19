import { createSlice } from "@reduxjs/toolkit"

export const modalSlice = createSlice({
  name: "modal",
  initialState: {
    show: false,
  },
  reducers: {
    SHOW: (state) => {
      state.show = true
    },
    HIDE: (state) => {
      state.show = false
    },
  },
})

export const { SHOW, HIDE } = modalSlice.actions

export default modalSlice.reducer
