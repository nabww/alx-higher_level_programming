#!/usr/bin/node
//count number of args

if (process.argv.length === 1)
{
	console.log('Argument found');
}else if (process.argv.length > 2)
{
	console.log('Arguments found');
}else console.log('No argument')
