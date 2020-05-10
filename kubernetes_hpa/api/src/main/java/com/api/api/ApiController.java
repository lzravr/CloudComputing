package com.api.api;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping(path = "/api")
@CrossOrigin(origins = "*")
public class ApiController {

	@GetMapping(path = "/metod1")
	public @ResponseBody String serveRequest(@RequestParam int kolicinaMemorije) throws InterruptedException {
		byte[] niz = new byte[kolicinaMemorije * 1024 * 1024];
		System.out.println("Allocated " + niz.length + " bytes");
		niz = null;
		Thread.sleep(500);
		System.out.println("Freed");
		return "OK";
	}
}
