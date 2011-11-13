# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Add a new task</h1>

<form action="${request.route_url('new')}" method="post">
  <input type="text" maxlength="100" name="name">
  <input type="submit" name="add" value="Add" class="button">
</form>
<p>
<a href="${request.route_url('list')}">Back to list</a>
</p>