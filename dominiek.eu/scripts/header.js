var dbg;

var clFree = "#19BAFF";
var clTaken = "#47FF19";
var blocked = Array();

function initHeader(handle)
{
	var paper = Raphael(handle, "100%", "100%");
	dbg = paper;
	var grid = initGrid(paper, 10, 10, 10);
	
	//window.setInterval(function() { (function(grid) { loopGOL(grid); })(grid) }, 100);
}

function initGrid(paper, side)
{
	var grid = Array();
	
	var rows = (paper.canvas.clientHeight) / side;
	var cols = (paper.canvas.clientWidth) / side;
	
	for (row=0; row < rows; row++)
	{
		grid[row] = Array();
		
		for (col=0; col < cols; col++)
		{
			var rect = paper.rect(col * side, row * side, side, side);
			rect.attr("fill", clFree);
			rect.attr("stroke", "#fff");
			grid[row][col] = rect;
			
			rect.taken = false;
			rect.grid = grid;
			rect.row = row;
			rect.col = col;
			rect.mouseover((function(rect) { return function() { mouseOver(rect); } })(rect));
			rect.mouseout((function(rect) { return function() { mouseOut(rect); } })(rect));
			rect.mousedown((function(rect) { return function() { mouseClick(rect); } })(rect));
		}
	}
	
	return grid;
}

function mouseOver(rect)
{
	//toggle(rect);
}

function mouseOut(rect)
{
	//toggle(rect);
}

function setTaken(rect, taken)
{
	if (rect.taken == taken)
	{
		return;
	}
	
	rect.taken = taken;
	
	var newfill =  clFree;
	
	if (rect.taken)
	{
		newfill = clTaken;
	}
	
	var animation = Raphael.animation({fill: newfill}, 100);
	rect.animate(animation);
}

function toggle(rect)
{
	setTaken(rect, !getTaken(rect));
}

function getTaken(rect)
{
	return rect.taken;
}

function mouseClick(rect)
{
	setTaken(rect, true);
	//alert(countNeighbours(rect));
}

function loopGOL(grid)
{
	var live = Array();
	var dead  = Array();
	
	for (row = 0; row < grid.length; row++)
	{
		for (col = 0; col < grid[row].length; col++)
		{
			var rect = grid[row][col];
			var neighbours = countNeighbours(rect);
			
			if ( (neighbours == 3) && (!getTaken(rect)) )
			{
				live.push(rect);
			} else if ( ((neighbours == 2) || (neighbours == 3)) && getTaken(rect) )
			{
				live.push(rect);
			} else {
				dead.push(rect);
			}
		}	
	}
	
	$.each(live, function(i, v) { setTaken(v, true); });
	$.each(dead, function(i, v) { setTaken(v, false); });
}

function countNeighbours(rect)
{
	var grid = rect.grid;
	var row = rect.row;
	var col = rect.col;
	
	return  isTaken(grid, row - 1, col - 1) +
			isTaken(grid, row - 1, col - 0) +
			isTaken(grid, row - 1, col + 1) +
			isTaken(grid, row - 0, col - 1) +
			isTaken(grid, row - 0, col + 1) +
			isTaken(grid, row + 1, col - 1) +
			isTaken(grid, row + 1, col - 0) +
			isTaken(grid, row + 1, col + 1);
}

function isTaken(grid, row, col)
{
	if ( (row >= 0) && (row < grid.length)
			&& (col >= 0) && (col < grid[0].length) )
			{
				return (grid[row][col].taken == true) ? 1 : 0;
			} else {
				return 0;
			}
}