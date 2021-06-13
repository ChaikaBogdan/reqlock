import React, { useState, useEffect } from "react";
import { UncontrolledDiagram } from "./Diagram.jsx";
import { BACKEND_URL } from "../constants.js";
import axios from "axios";
import _ from "lodash";

const apiUrl = `${BACKEND_URL}/api`;

export const Projects = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    axios.get(`${apiUrl}/projects/`).then((res) => {
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
    return <UncontrolledDiagram initialSchema={projectsSchema} />;
  }
  return null;
};
