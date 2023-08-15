import React from "react";

import { List } from "reactstrap";
function Form(props) {
  return (
    <div>
      <List className="animate-charcter">
        <li>W.Areej</li>
        <li>areejwesleti@gmail.com</li>
        <li>WebDevper</li>
        <li>{props.adresse}</li>
      </List>
    </div>
  );
}

export default Form;
