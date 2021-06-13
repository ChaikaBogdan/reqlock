import React, { useState, useEffect } from "react";
import { UncontrolledDiagram } from "./Diagram.jsx";
import { BACKEND_URL } from "../constants.js";
import axios from "axios";
import _ from "lodash";

const apiUrl = `${BACKEND_URL}/api`;

export const Projects = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    console.log("Projects UseEffect triggered");
    axios.get(`${apiUrl}/projects/`).then((res) => {
      console.log("Axios getting projects and setting state");
      setProjects(res.data);
    });
  }, []);
  const projectsSchema = {
    nodes: projects.map((project) => ({
      id: project.id.toString(),
      content: project.name,
      coordinates: [100, 100],
    })),
  };
  if (projects.length) {
    console.log("Projects rendering UncontrolledDiagram");
    return <UncontrolledDiagram initialSchema={projectsSchema} />;
  }
  return null;
};
