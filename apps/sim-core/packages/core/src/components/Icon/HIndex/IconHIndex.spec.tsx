import React from "react";
import ReactDOM from "react-dom";

import { IconHIndex } from "./IconHIndex";

it("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(<IconHIndex />, div);
  ReactDOM.unmountComponentAtNode(div);
});
