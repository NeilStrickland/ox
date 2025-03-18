This repository contains code for playing the game Noughts and Crosses (also known as Tic-Tac-Toe).  It is mostly intended as a simple example of a Python package containing several files with relative imports.

The noughts and crosses board has nine spaces, which we number in the obvious way as follows:
<table>
 <tr>
  <td style="border-right: 1px solid white; border-bottom: 1px solid white">0</td>
  <td style="border-left: 1px solid white; border-right: 1px solid white; border-bottom: 1px solid white">1</td>
  <td style="border-left: 1px solid white; border-bottom: 1px solid white">2</td>
 </tr>
 <tr>
  <td style="border-right: 1px solid white; border-bottom: 1px solid white">3</td>
  <td style="border-left: 1px solid white; border-right: 1px solid white; border-bottom: 1px solid white">4</td>
  <td style="border-left: 1px solid white; border-bottom: 1px solid white">5</td>
 </tr>
 <tr>
  <td style="border-right: 1px solid white; border-top: 1px solid white">6</td>
  <td style="border-left: 1px solid white; border-right: 1px solid white; border-top: 1px solid white">7</td>
  <td style="border-left: 1px solid white; border-top: 1px solid white">8</td>
 </tr>
</table>
When playing the game, we might reach a state like this:
<table>
 <tr>
  <td style="border-right: 1px solid white; border-bottom: 1px solid white">O</td>
  <td style="border-left: 1px solid white; border-right: 1px solid white; border-bottom: 1px solid white">O</td>
  <td style="border-left: 1px solid white; border-bottom: 1px solid white">O</td>
 </tr>
 <tr>
  <td style="border-right: 1px solid white; border-bottom: 1px solid white"></td>
  <td style="border-left: 1px solid white; border-right: 1px solid white; border-bottom: 1px solid white">X</td>
  <td style="border-left: 1px solid white; border-bottom: 1px solid white"></td>
 </tr>
 <tr>
  <td style="border-right: 1px solid white; border-top: 1px solid white">X</td>
  <td style="border-left: 1px solid white; border-right: 1px solid white; border-top: 1px solid white"></td>
  <td style="border-left: 1px solid white; border-top: 1px solid white">X</td>
 </tr>
</table>
This will be represented in Python by the array <code>pq = [[1,0],[1,0],[1,0],[0,1],[0,0],[0,1],[0,0],[0,1],[0,0]]</code> of shape <code>(9,2)</code>.  In more detail there are Os in spaces 0, 1 and 2, so the first column of the array <code>pq</code> is the vector with ones in positions 0, 1 and 2 and zeros everywhere else.  Similarly, there are Xs in positions 3, 5 and 7, so the second column of <code>pq</code> is the vector with ones in positions 3, 5 and 7, and zeros everywhere else.

All the functions in this package will operate on arrays of this form.
