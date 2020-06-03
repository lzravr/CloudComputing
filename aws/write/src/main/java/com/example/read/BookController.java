package com.example.read;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller // This means that this class is a Controller
@RequestMapping(path = "/books")
@CrossOrigin(origins = "*")
public class BookController {
	public final AtomicLong id = new AtomicLong(1);
	@Autowired
	private BookRepository bookRepository;
	
	@PostMapping(path="/add") 
	  public @ResponseBody String addNewUser (@RequestParam String title
	      , @RequestParam String author, @RequestParam String genre, @RequestParam String year) {
		
		Book b = new Book();
		b.setAuthor(author);
		b.setGenre(genre);
		b.setTitle(title);
		b.setYear(year);
		bookRepository.save(b);
	    return "Saved";
	  }
}
